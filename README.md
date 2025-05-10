# Celery Broadcast Bug Report

## How to Run

1. Ensure you have Docker installed on your system.
2. Navigate to the project directory:
   ```bash
   cd /path/to/celery-bcast-bug-report
   ```
3. Start the services using Docker Compose:
   ```bash
   docker compose up
   ```
   If you want to run the services in detached mode (in the background), use:
   ```bash
   docker compose up -d
   ```

## Checking the Logs

To observe the bug, check the logs of the `celery_worker_direct` container:

```bash
docker logs -f celery-bcast-bug-report_celery_worker_direct_1
```

Replace `celery-bug-report_celery_worker_direct_1` with the actual container name if it differs.

Logs should contain something along the lines of:

```
[2025-05-10 00:21:23,611: DEBUG/MainProcess] Binding queue 'bcast.d12d36c1-b6b4-43b2-81f2-c04100db93f2' to delayed delivery exchange


[2025-05-10 00:21:23,611: DEBUG/MainProcess] using channel_id: 3


[2025-05-10 00:21:23,614: DEBUG/MainProcess] Channel open


[2025-05-10 00:21:23,624: DEBUG/MainProcess] Channel open


[2025-05-10 00:21:23,628: ERROR/MainProcess] Failed to bind queue 'bcast.d12d36c1-b6b4-43b2-81f2-c04100db93f2': Queue.bind: (404) NOT_FOUND - no queue 'bcast.d12d36c1-b6b4-43b2-81f2-c04100db93f2' in vhost '/'


[2025-05-10 00:21:23,628: WARNING/MainProcess] Failed to bind queues for 'amqp://user:password@rabbitmq:5672//': Queue.bind: (404) NOT_FOUND - no queue 'bcast.d12d36c1-b6b4-43b2-81f2-c04100db93f2' in vhost '/'


[2025-05-10 00:21:23,628: WARNING/MainProcess] Failed to setup delayed delivery for 'amqp://user:password@rabbitmq:5672//': Queue.bind: (404) NOT_FOUND - no queue 'bcast.d12d36c1-b6b4-43b2-81f2-c04100db93f2' in vhost '/'


[2025-05-10 00:21:23,628: CRITICAL/MainProcess] Failed to setup delayed delivery for all broker URLs. Native delayed delivery will not be available.
```