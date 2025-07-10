from loguru import logger

def final_cart_amount(*args, discount=0.1):
    try:
        result = 0
        for amount in args:
            result+= amount

        amount_after_discount = result - (result*discount)

        return amount_after_discount
    except TypeError:
        logger.info("Plz provide the amount in integer")
    
    except Exception as e:
        logger.info("Can not process the cart amount")
        # raise e         # TypeError




final_amount_to_be_paid = final_cart_amount(100, 500, 120, 300, '500', discount=0.5)

logger.info(final_amount_to_be_paid)

logger.info("End...")

