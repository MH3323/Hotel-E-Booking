import json
from tkinter.messagebox import NO
import user
import hotel
import bill
import time


# These function are used to read, write and replace data of hotel in json file
def read_hotel_data(file_path):
    with open(file_path, "r") as json_file:
        json_object = json.load(json_file)
        return json_object


def get_hotel_info(list_hotel, number_of_hotel):
    request = 'y'
    while request == 'y' or request == 'Y':
        name = input("Enter hotel name: ")
        address = input("Enter hotel address: ")
        number_of_room = int(input("Enter number of room: "))
        hotel_id = hotel.Hotel.create_hotel_id(number_of_hotel)
        temp_hotel = hotel.Hotel(hotel_id, name, address, number_of_room)
        for i in range(number_of_room):
            room_type = input("Enter room type: ")
            room_price = int(input("Enter room price: "))
            room_availability = True
            user_book = None
            date_check_in = None
            date_check_out = None
            description = input("Enter description: ")
            image_path = None
            room_id = hotel.Room.create_room_id(hotel_id, i, room_type)
            temp_room = hotel.Room(room_id, room_type, room_price, room_availability,
                                   user_book, date_check_in, date_check_out, description, image_path)
            temp_hotel.list_room.append(temp_room)
        number_of_hotel += 1
        list_hotel.append(temp_hotel)
        request = input("Do you want to add more hotel? (y/n) ")


def convert_class_hotel_to_json(list_of_hotel, number_of_hotel):
    json_hotel = "{\"number_of_hotel\": " + \
        str(number_of_hotel) + ","+"\"hotel\": ["
    for i in range(len(list_of_hotel)):
        json_hotel += "{\"hotel_id\":" + "\"" + list_of_hotel[i].hotel_id + "\"," + "\"hotel_name\":" + "\"" + list_of_hotel[i].hotel_name + "\"," + "\"hotel_address\":" + \
            "\"" + list_of_hotel[i].hotel_address + "\"," + "\"number_available_room\":" + \
            "\"" + \
            str(list_of_hotel[i].number_available_room) + "\"," + "\"room\": ["
        for j in range(len(list_of_hotel[i].list_room)):
            json_hotel += json.dumps(list_of_hotel[i].list_room[j].__dict__)
            if j != len(list_of_hotel[i].list_room)-1:
                json_hotel += ","
        json_hotel += "]}"
        if i != len(list_of_hotel)-1:
            json_hotel += ","
    json_hotel += "]}"
    json_object = json.loads(json_hotel)
    return json.dumps(json_object, indent=4)


def convert_json_to_class_hotel(json_object):
    list_of_hotel = []
    number_of_hotel = json_object["number_of_hotel"]
    for i in range(number_of_hotel):
        hotel_id = json_object["hotel"][i]["hotel_id"]
        hotel_name = json_object["hotel"][i]["hotel_name"]
        hotel_address = json_object["hotel"][i]["hotel_address"]
        number_available_room = json_object["hotel"][i]["number_available_room"]
        temp_hotel = hotel.Hotel(hotel_id, hotel_name,
                                 hotel_address, number_available_room)
        for j in range(len(json_object["hotel"][i]["room"])):
            room_id = json_object["hotel"][i]["room"][j]["room_id"]
            room_type = json_object["hotel"][i]["room"][j]["room_type"]
            room_price = json_object["hotel"][i]["room"][j]["room_price"]
            room_availability = json_object["hotel"][i]["room"][j]["room_availability"]
            user_book = json_object["hotel"][i]["room"][j]["user_book"]
            date_check_in = json_object["hotel"][i]["room"][j]["date_check_in"]
            date_check_out = json_object["hotel"][i]["room"][j]["date_check_out"]
            description = json_object["hotel"][i]["room"][j]["description"]
            image_path = json_object["hotel"][i]["room"][j]["image_path"]
            temp_room = hotel.Room(room_id, room_type, room_price, room_availability,
                                   user_book, date_check_in, date_check_out, description, image_path)
            temp_hotel.list_room.append(temp_room)
        list_of_hotel.append(temp_hotel)
    return list_of_hotel


def print_all_hotel(list_hotel):
    for hotel in list_hotel:
        print(hotel.hotel_id, hotel.hotel_name, hotel.hotel_address,
              hotel.number_available_room)
        for room in hotel.list_room:
            print(room.room_id, room.room_type,
                  room.room_price, room.room_availability)


def main():
    list_of_hotel = []
    number_of_hotel = 0
    # Create Data Hotel


if __name__ == "__main__":
    main()