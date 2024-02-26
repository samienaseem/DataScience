#Here when we import this model and print method is executed it says Model but niot main because it executed by model.py
print(__name__)

def greater(name):
    return "Good Morning " + name

def main(): 
    print("This is main function")
    print("This is execute when name is main")

#to hide the sensitive content from anyone directly calling the model

if __name__=="__main__":
    print('This is confidential code')
    main()