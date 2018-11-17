echo "** Creating superuser admin **"
python3 manage.py createsuperuser --noinput --username admin --email admin@admin.com --name admin --registry 101010 
printf "superuser\nsuperuser" | python3 manage.py changepassword admin
