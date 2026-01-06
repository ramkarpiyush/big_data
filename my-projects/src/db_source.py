import re


class DB_Source(Source):
    def read_data(self, spark, DI_Config, encode_cols, di_input, di_output):
        if di_input.load_type == 'TRUNCATE/INSERT' or di_input.load_type == 'DELETE/INSERT':
            data_df = self.read_full_data(spark, di_input, di_output)
        elif di_input.load_type == 'APPEND' or di_input.load_type == 'UPSERT':
            data_df = self.read_incr_data(spark, DI_Config, di_input, di_output)
        else :
            raise Exception('Load Type can be : TRUNCATE/INSERT, DELETE/INSERT, APPEND OR UPSERT!!')
        #di_output.row_count = data_df.count()
        #print('row count : ' + str(di_output.row_count))
        return data_df
    
    def get_conn_properties(self, di_input):
        db_properties = {}
        db_properties['user'] = di_input.src_user
        db_properties['password'] = di_input.src_password
        db_properties['driver'] = di_input.src_driver
        db_properties['fetchsize'] = str(di_input.src_fetchsize)
        if not Utility.is_null_or_empty(di_input.num_partitions):
            db_properties['numPartitions'] = str(di_input.num_partitions)
        if not Utility.is_null_or_empty(di_input.split_by_col):
            db_properties['partitionColumn'] = di_input.split_by_col.strip()
        return db_properties
        
    def set_lower_n_upper_bounds(self, spark, db_properties, di_input):
        print('Fetching lower and upper bounds for partition..')
        query="select min(" + db_properties['partitionColumn'] + ") min_val, max(" + db_properties['partitionColumn'] + ") max_val from " + di_input.fully_qualified_src_table_name
        lower_n_upper_bound_df=self.read_data_using_query(spark, di_input, query)
        temp=lower_n_upper_bound_df.collect()
        db_properties['lowerBound']=str(temp[0][0])
        db_properties['upperBound']=str(temp[0][1])
        
    def read_data_using_query(self, spark, di_input, query):
        print(query)
        df=spark.read.format("jdbc")\
            .option("url", di_input.src_jdbc_url)\
            .option("driver", di_input.src_driver)\
            .option("query", query)\
            .option("user", di_input.src_user)\
            .option("password", di_input.src_password)\
            .option("fetchsize", str(di_input.src_fetchsize))\
            .load()
        return df
        
    def read_full_data(self, spark, di_input, di_output):
        if not Utility.is_null_or_empty(di_input.src_query):
            di_output.src_query = di_input.src_query
            print('Fetching data using query : ' + di_input.src_query)
            return self.read_data_using_query(spark, di_input, di_input.src_query)
        else:
            di_output.src_table = di_input.fully_qualified_src_table_name
            db_properties=self.get_conn_properties(di_input)
            if not Utility.is_null_or_empty(db_properties.get('partitionColumn')):
                di_output.split_by_col = db_properties['partitionColumn']
                di_output.num_partitions = int(db_properties.get('numPartitions'))
                self.set_lower_n_upper_bounds(spark, db_properties, di_input)
            Utility.print_db_properties(db_properties)
            return spark.read.jdbc(url=di_input.src_jdbc_url, table=di_input.fully_qualified_src_table_name, properties=db_properties)
