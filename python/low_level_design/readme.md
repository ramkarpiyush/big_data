# LOW LEVEL DESIGN: Data Ingestion Framework
- Application of Factory method and Abstract factory design pattern

- Requirements:
    1. Fetch data from multiple sources
    2. New source can be onboarded at anytime without affecting any change to the existing sources.
    3. source can provide data using any method as per the convenience like file share, expose an API etc.
    4. We have large scale distributed system, so part of the data resides in on=premises storage and part on public cloud.
    5. Decision to store data to on premise or cloud should be made on the fly based on some parameter

```
                                            **Data Source**         
                
                                            Read API
                    Ingest on premises                                        
Ingestion Service                           Read file                   
                    Ingest on cloud                                        
                                            Read Database

```
                                           