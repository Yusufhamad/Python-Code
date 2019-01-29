path = r"E:\Data\GIS\case_num.csv"
file = open(path, 'w')
header_line = ("ID, Case_Number, Number_of_people" + "\n")
file.write(header_line)
for x in range (0, number_records_create):
    record_id = str(x)
    import random
    city = ("388", "191", "196")
    city_r = str(random.choice(city))
    year = ("12", "13", "14")
    year_r = str(random.choice(year))
    iden = str(random.randint(10000, 99999))
    case = city_r + "-" + year_r + "C" + iden
    record_num = str(random.randint(1, 20))
    out_put = record_id + "," + case + "," + record_num + "\n"
    file.write(out_put)
file.close()

 
	

	


