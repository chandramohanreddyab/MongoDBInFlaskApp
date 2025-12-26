from flask import Flask,render_template, request
import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId
import certifi


load_dotenv('/Users/chandra/Courses/MLProjects/MongoDBInFlaskApp/.env')
MONGODB_URI = os.getenv('MONGO_DB_URL') 
client = pymongo.MongoClient(
    os.environ.get("MONGO_DB_URL"),
    tls=True,
    tlsCAFile=certifi.where())

db= client['employee_db']
employees_skills = db['employees_skillset']

app=Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/entry', methods=['GET','POST'])
def entry():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        skill = request.form['skills'].strip().split(',')
        print(skill)
        city = request.form['city']
        country = request.form['country']
        
        employee_data = {   
            'first_name': first_name,
            'last_name': last_name,
            'skills': skill,
            'city': city,
            'country': country
        }
        
        result = employees_skills.insert_one(employee_data)
        return render_template('entry.html', employee=employee_data)
    #     return render_template('entry.html', employee_id=str(result.inserted_id))
    # # Render a page that can display a recently entered employee if provided
    # employee_id = request.args.get('id')
    # employee = None
    # if employee_id:
    #     try:
    #         employee = employees_skills.find_one({'_id': ObjectId(employee_id)})
    #     except Exception:
    #         employee = None
    # return render_template('entry.html', employee=employee)



@app.route('/query',methods=['GET','POST'])
def query():
    # read parameters (support GET and POST)
    vals = request.values
    q = vals.get('q','').strip()
    first_name = vals.get('first_name','').strip()
    last_name = vals.get('last_name','').strip()
    skill = vals.get('skill','').strip()
    city = vals.get('city','').strip()
    country = vals.get('country','').strip()

    filters = []

    if q:
        regex = {'$regex': q, '$options': 'i'}
        filters.append({'$or': [
            {'first_name': regex},
            {'last_name': regex},
            {'city': regex},
            {'country': regex},
            {'skills': regex}
        ]})

    if first_name:
        filters.append({'first_name': {'$regex': first_name, '$options': 'i'}})
    if last_name:
        filters.append({'last_name': {'$regex': last_name, '$options': 'i'}})
    if city:
        filters.append({'city': {'$regex': city, '$options': 'i'}})
    if country:
        filters.append({'country': {'$regex': country, '$options': 'i'}})
    if skill:
        # match skill inside skills array (case-insensitive)
        filters.append({'skills': {'$regex': skill, '$options': 'i'}})

    if filters:
        if len(filters) == 1:
            mongo_query = filters[0]
        else:
            mongo_query = {'$and': filters}
    else:
        mongo_query = {}

    cursor = employees_skills.find(mongo_query).sort('first_name', 1)
    employees = []
    for doc in cursor:
        doc['_id'] = str(doc['_id'])
        employees.append(doc)

    # pass 'skill' for the template header logic (template checks this variable)
    return render_template('query.html', employees=employees, skill=skill)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True,port=port, host='0.0.0.0')