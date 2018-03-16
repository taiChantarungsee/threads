#Script to import all the CSV data into a django model
import csv, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "threads_styling.settings")
import django
django.setup()
from reports.models import district

with open('2016_fixed_ctyua_r01.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[0] != 'la_code':
			_, created = district.objects.get_or_create(
				la_code=row[0],
				la_name = row[1],
				average_download_speed = row[10],)

district = district.objects.first()
print("Script finished!", district.average_download_speed)