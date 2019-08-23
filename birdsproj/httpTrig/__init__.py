import logging

import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    message = req.params.get('message')
    if not message:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            message = req_body.get('message')

    if message:
        logging.info(f"Your message was: {message}")
        msg.set(message)
        return func.HttpResponse(f"Your message was: {message}")
    else:
        return func.HttpResponse(
             "Please pass a message on the query string or in the request body",
             status_code=400
        )
