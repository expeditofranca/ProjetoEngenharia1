#!/bin/sh
# wait-for-it.sh
set -e
host="$1"
shift
until pg_isready -h "$host" -p 5432; do
  echo "Aguardando PostgreSQL em $host..."
  sleep 2
done
echo "PostgreSQL está pronto - executando comandos..."
exec "$@"