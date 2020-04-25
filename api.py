import requests,json, os


path = './courses.json'
    
isExist = os.path.exists(path)  
if (isExist):
	with open('courses.json','r') as file_open:
		new_data = json.load(file_open)
		# print(new_data)
		count = 1
		id_list = []
		for i in new_data["availableCourses"]:
			print(count,i.get("name"))
			count = count + 1
			id_list.append(i.get("id"))
		# print(id_list)



		user = int(input("\nenter the number "))
		count1 = 1
		slug_list = []
		id_request = requests.get("http://saral.navgurukul.org/api/courses/"+str(id_list[user-1])+"/exercises")
		# id_data = id_request.json()
		p = (id_request.json())

		for k in p ["data"]:
			print(count1,k.get( "name"))
			count1 = count1 + 1
			slug_list.append(k.get("slug"))
		# print(slug_list)


		user2 = int(input("\nEnter The number "))
		# print(slug_list[user2-1])
		slugList_request = requests.get("http://saral.navgurukul.org/api/courses/"+str(id_list[user2-1])+"/exercise/getBySlug?slug="+ slug_list[user2-1])
		# print(slugList_request)

		qw = (slugList_request.json())
		print(qw.get("content"))
		
else:
	new = requests.get('http://saral.navgurukul.org/api/courses')
	courses_data=new.json()


	with open('courses.json','w') as push:
		json.dump(courses_data,push)
		print("file is dump")


