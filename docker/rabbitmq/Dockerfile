FROM rabbitmq:3.13.1

# Start with a clean rabbitmq conf
RUN rm -f /etc/rabbitmq/rabbitmq.conf

# RabbitMQ configuration
RUN echo "management.tcp.port = 15672" >> /etc/rabbitmq/rabbitmq.conf
RUN echo "management.tcp.ip   = 0.0.0.0" >> /etc/rabbitmq/rabbitmq.conf

# Expose the default RabbitMQ port
EXPOSE 5672
EXPOSE 15672