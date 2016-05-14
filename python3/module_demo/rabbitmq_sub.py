#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='fanout_logs', type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='fanout_logs', queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')
def callback(ch, method, properties, body):
    print(body)
channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
