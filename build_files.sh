echo "BUILD START"
python3.11.2  manage.py collectstatic --noinput --clear
echo "BUILD END" 