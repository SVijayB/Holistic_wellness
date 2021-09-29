class Fitness:
    def __init__(self):
        self.calories=0.0

    @staticmethod
    def calories_burnt(activity,duration):
        if activity=="cycling":
            calories=10*duration
            return calories
        elif activity=="jogging":
            calories=11.4*duration
            return calories
        elif activity=="walking":
            calories=6.5*duration
            return calories
        elif activity=="yoga":
            calories=5*duration
            return calories
        elif activity=="gym":
            calories=7*duration
            return calories
        else:
            calories=10.5*duration
            return calories

    @staticmethod
    def suggest_bmi(bmi):
        if bmi<18.5:
            suggestion="You fall under under weight! You need to start consuming more calories everyday to gradually increase weight. Food items with high protein is recommended."
        elif bmi>18.5 and bmi<24.9:
            suggestion="Congratulations, you are have a perfect bmi. Keep up the same routine and do include yoga and exercise."
        elif bmi>25 and bmi<30:
            suggestion="You fall under over weight, For having a healthy body, You need to put down weight. Start consuming more of salads, vegetables and reduce junk food/over eating. Do starting working out to burn excess fat"
        else:
            suggestion="You need immediate medical attention, do consult a dietician for getting a diet plan. You need to start burning calories everyday."
        return suggestion

    def suggest_calories_breakfast(breakfast,bmi):
        if breakfast==0:
            suggestion1="You will be suggested only after you enter some of your consumption details!"
        #breakfast
        elif breakfast<=350 and bmi<=18:
            suggestion1="Your intake of calories is too less for breakfast. You need to start having in surplus(more than ideal) to put on weight!"
        elif breakfast>350 and bmi<18:
            suggestion1="You have a good consumption routine for breakfast, continue the same, you'll gain weight soon! Keep us updated"
        elif breakfast<350 and bmi>24:
            suggestion1="Good, you will reduce your weight soon! Do update your height and weight regularly"
        elif breakfast>350 and bmi>=24:
            suggestion1="You are consuming more than you should for breakfast! Reduce intake for weight loss!"
        elif breakfast>300 and breakfast<400 and bmi>18 and bmi<24:
            suggestion1="You have a good food routine as well as bmi. Continue the same!"
        elif breakfast<300 and bmi>18 and bmi<24:
            suggestion1="You will have to consume more calories, Do refer the ideal graph for a good diet!"
        elif breakfast>400 and bmi>18 and bmi<24:
            suggestion1="Your intake is a little more than required, try reducing intake a little."
        return suggestion1

        #lunch
    def suggest_calories_lunch(lunch,bmi):
        if lunch==0:
            suggestion2="You will be suggested only after you enter some of your consumption details!"
        elif lunch<=700 and bmi<=18:
            suggestion2="Your intake of calories is too less for lunch. You need to start having in surplus(more than ideal) to put on weight!"
        elif lunch>700 and bmi<18:
            suggestion2="You have a good consumption routine for lunch, continue the same, you'll gain weight soon! Keep us updated"
        elif lunch<700 and bmi>24:
            suggestion2="Good, you will reduce your weight soon! Do update your height and weight regularly"
        elif lunch>700 and bmi>=24:
            suggestion2="You are consuming more than you should for lunch! Reduce intake for weight loss!"
        elif lunch>650 and lunch<750 and bmi>18 and bmi<24:
            suggestion2="You have a good food routine as well as bmi. Continue the same!"
        elif lunch<650 and bmi>18 and bmi<24:
            suggestion2="You will have to consume more calories, Do refer the ideal graph for a good diet!"
        elif lunch>750 and bmi>18 and bmi<24:
            suggestion2="Your intake is a little more than required, try reducing intake a little."
        return suggestion2

        #dinner
    def suggest_calories_dinner(dinner,bmi):
        if dinner==0:
            suggestion3="You will be suggested only after you enter some of your consumption details!"
        elif dinner<=500 and bmi<=18:
            suggestion3="Your intake of calories is too less for dinner. You need to start having in surplus(more than ideal) to put on weight!"
        elif dinner>500 and bmi<18:
            suggestion3="You have a good consumption routine for dinner, continue the same, you'll gain weight soon! Keep us updated"
        elif dinner<500 and bmi>24:
            suggestion3="Good, you will reduce your weight soon! Do update your height and weight regularly"
        elif dinner>500 and bmi>=24:
            suggestion3="You are consuming more than you should for dinner! Reduce intake for weight loss!"
        elif dinner>450 and dinner<550 and bmi>18 and bmi<24:
            suggestion3="You have a good food routine as well as bmi. Continue the same!"
        elif dinner<450 and bmi>18 and bmi<24:
            suggestion3="You will have to consume more calories, Do refer the ideal graph for a good diet!"
        elif dinner>550 and bmi>18 and bmi<24:
            suggestion3="Your intake is a little more than required, try reducing intake a little."
        return suggestion3