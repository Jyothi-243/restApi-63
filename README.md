Rest framework working in django , added rest framework in installled apps of settings.py ,added application in that also.
Added serializers.py in quickstart application 
Serializers are used to convert the query set in to JSON format like key:value pairs
created the model(Student) in models.py 
In serializers created a StudentSerializer 
http://127.0.0.1:8000/admin , login as user and added students
In views.py , created apiview, used model(student) and serializer and get the output of student as json format
