import time
import uuid
from database import Database
import datetime
from flask import session
from fitness import Fitness

class User:
    def __init__(self,name,age,gender,height,weight,email,password,bmi,time=time.time(),calories=0,_id=None,breakfast=0,lunch=0,snacks=0,dinner=0):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
        self.email=email
        self.password=password
        self.bmi=round(bmi,2)
        self.time=time
        self.calories=calories
        self.breakfast=breakfast
        self.lunch=lunch
        self.snacks=snacks
        self.dinner=dinner
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("user_details", {"email": email})
        if data is not None:
            return cls(**data)
    
    @classmethod
    def get_name(cls,email):
        user=User.get_by_email(email)
        return user.name

    @classmethod
    def get_breakfast(cls,email):
        user=User.get_by_email(email)
        return user.breakfast

    @classmethod
    def get_lunch(cls,email):
        user=User.get_by_email(email)
        return user.lunch

    @classmethod
    def get_snacks(cls,email):
        user=User.get_by_email(email)
        return user.snacks

    @classmethod
    def get_dinner(cls,email):
        user=User.get_by_email(email)
        return user.dinner
    
    @classmethod
    def get_bmi(cls,email):
        user=User.get_by_email(email)
        return user.bmi

    @classmethod
    def get_calories(cls,email):
        user=User.get_by_email(email)
        return user.calories

    @classmethod
    def get_age(cls,email):
        user=User.get_by_email(email)
        return user.age

    @staticmethod
    def check_email(email):
        user=User.get_by_email(email)
        if(user is not None):
            session['email']=email
            return True
        return False

    @staticmethod
    def update_password(new_password):
        user=User.get_by_email(session['email'])
        value={"$set": {"password":new_password}}
        query={"password":user.password}
        Database.update("user_details",query,value)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False
    
    @classmethod
    def register(cls, name,age,gender,height,weight,email,password):
        user = cls.get_by_email(email)
        if user is None:
            bmi=float(weight/(height*height))
            new_user=User(name,age,gender,height,weight,email,password,bmi)
            new_user.save_to_mongo()
            session['name'] = name
            session['email'] = email
            session['bmi'] = new_user.bmi
            session['calories'] = new_user.calories
            session['age']=new_user.age
            session['breakfast'] = new_user.breakfast
            session['lunch'] = new_user.lunch
            session['snacks'] = new_user.snacks
            session['dinner']=new_user.dinner
            return True
        else:
            return False
    
    @staticmethod
    def login(user_email):
        session['email'] = user_email
        session['name'] = User.get_name(user_email)
        session['bmi'] = User.get_bmi(user_email)
        session['calories'] = User.get_calories(user_email)
        session['age']=User.get_age(user_email)
        session['breakfast'] = User.get_breakfast(user_email)
        session['lunch'] = User.get_lunch(user_email)
        session['snacks'] = User.get_snacks(user_email)
        session['dinner']=User.get_dinner(user_email)

    @staticmethod
    def add_calories(cal):
        cal=cal*1.5
        user=User.get_by_email(session['email'])
        today=datetime.datetime.now()
        if today.hour>6 and today.hour<=11:  #breakfast
            if (time.time() - user.time)>43200:
                total=(user.breakfast+cal)*2
            else:
                total=(user.breakfast+cal)*4
            session['breakfast']=total/2
            value={"$set": {"breakfast":(total)/2}}
            query={"breakfast":user.breakfast}
            Database.update("user_details",query,value)


        if today.hour>=12 and today.hour<=16:  #Lunch
            if (time.time() - user.time)>43200:
                total=user.lunch+cal
            else:
                total=(user.lunch+cal)*4

            session['lunch']=total/2
            value={"$set": {"lunch":(total)/2}}
            query={"lunch":user.lunch}
            Database.update("user_details",query,value)

        if today.hour>=17 and today.hour<=18:  #Snacks

            if (time.time() - user.time)>43200:
                total=user.snacks+cal
            else:
                total=(user.snacks+cal)*4

            session['snacks']=total/2
            value={"$set": {"snacks":(total)/2}}
            query={"snacks":user.snacks}
            Database.update("user_details",query,value)

        if today.hour>=19 and today.hour<=24:  #Dinner

            if (time.time() - user.time)>43200:
                total=user.dinner+cal
            else:
                total=(user.dinner+cal)*4
                    
            session['dinner']=total/2  
            value={"$set": {"dinner":(total)/2}}
            query={"dinner":user.dinner}
            Database.update("user_details",query,value)
        
        if (time.time() - user.time<43200):
            t=(time.time()-user.time)/(60*60)
            cal=cal-(t*20)
            cal=cal+user.calories
            value={"$set": {"calories":cal}}
            query={"calories":user.calories}
            Database.update("user_details",query,value)
            query={"time":user.time}
            value={"$set": {"time":time.time()}}
            Database.update("user_details",query,value)
        else:
            cal=cal+user.calories-20*5
            value={"$set": {"calories":cal}}
            query={"calories":user.calories}
            Database.update("user_details",query,value)
            query={"time":user.time}
            value={"$set": {"time":time.time()}}
            Database.update("user_details",query,value)
        session['calories']=cal
            
    @staticmethod
    def subtract_calories(activity,duration):
        user=User.get_by_email(session['email'])
        calories=Fitness.calories_burnt(activity,duration)
        if ( time.time() - user.time<43200):
            t=( time.time()- user.time)/(60*60)
            calories=calories+(t*46)
            final_calories=user.calories-calories
            print(final_calories)
            print(calories)
            value={"$set": {"calories":final_calories}}
            query={"calories":user.calories}
            Database.update("user_details",query,value)
            query={"time":user.time}
            value={"$set": {"time":time.time()}}
            Database.update("user_details",query,value)
        else:
            final_calories=user.calories-46*5-calories
            value={"$set": {"calories":final_calories}}
            query={"calories":user.calories}
            Database.update("user_details",query,value)
            query={"time":user.time}
            value={"$set": {"time":time.time()}}
            Database.update("user_details",query,value)
        session['calories']=final_calories

    @staticmethod
    def update_user_details(height,weight):
        user=User.get_by_email(session['email'])
        session['bmi']=weight/(height*height)

        value={"$set": {"height":height}}
        query={"height":user.height}
        Database.update("user_details",query,value)
        value={"$set": {"weight":weight}}
        query={"weight":user.weight}
        Database.update("user_details",query,value)
        value={"$set": {"bmi":session['bmi']}}
        query={"bmi":user.bmi}
        Database.update("user_details",query,value)
        session['height']=height
        session['weight']=weight

    @staticmethod
    def logout():
        session['email'] = None
        session['name'] = None
        session['bmi'] = None
        session['calories'] = None
    
    def json(self):
        return {
            "name":self.name,
            "age":self.age,
            "gender":self.gender,
            "height":self.height,
            "weight":self.weight,
            "bmi":self.bmi,
            "calories":self.calories,
            "email": self.email,
            "password": self.password,
            "time":self.time,
            "breakfast":self.breakfast,
            "lunch":self.lunch,
            "snacks":self.snacks,
            "dinner":self.dinner
        }
    
    def save_to_mongo(self):
        Database.insert("user_details", self.json())