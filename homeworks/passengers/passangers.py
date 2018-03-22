# -*- encoding: utf-8 -*-


def process(trains, events, car):
    '''
        ТУТ ДОЛЖЕН БЫТЬ ВАШ КОД
    '''

    event_log(events)
    trains_log(trains)
    for event in events:
        prov=event_creator(event,trains)
        if prov==-1:
            return -1
    for train in trains:
        for car_of_function in train['cars']:
            if car==car_of_function['name']:
                result=len(car_of_function['people'])
    return result

def event_creator(event, trains):
    if event["type"]=="walk":
        for train in trains:
            for car in train['cars']:
                if 0!=car["people"].count(event["passenger"]):
                    car_number = train['cars'].index(car)+int(event['distance'])
                    if (car_number<0)or((len(train['cars'])-1)<car_number):
                        return -1
                    else:
                        name = event['passenger']
                        train['cars'][car_number]["people"].append(name)
                        train['cars'][train['cars'].index(car)]["people"].remove(event['passenger'])
                        return 1
    elif event["type"]=="switch":
        s=list()
        for train in trains:
            if train['name'] == event['train_from']:
                if len(train['cars'])<event['cars']:
                    return -1
                else:
                    for i in range(event['cars']):
                        test_iterator = event['cars']-i
                        s.append(train['cars'][len(train['cars']) - test_iterator])
                        del (train['cars'][len(train['cars']) - test_iterator])
        for train in trains:
            if train['name']== event['train_to']:
                train['cars'].extend(s)
        return 1
    else:
        print("error")
    print("end of change function")

def event_log(events):
    print("События:\n")
    for event in events:
        if event['type']=='walk':
            print('\tПасажир:',event['passenger'])
            print('\tЧто делает:', event['type'])
            print('\tРасстояние:', event['distance'],'\n')
        else:
            print('\tКоличество ваглнов', event['cars'])
            print('\tОткуда', event['train_from'])
            print('\tЧто происходит', event['type'])
            print('\tкуда', event['train_to'], '\n')
def trains_log (trains):
    for train in trains:
        print("поезд -", train['name'])
        for car_of_function in train['cars']:
            print("\tВагон -", car_of_function['name'])
            for man in car_of_function['people']:
                print("\t\tПасажир -", man)