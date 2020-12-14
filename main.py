from conatus.decode_file import Decode
from services.database_connection import Connection


def main() -> int:
    decode = Decode("Afternoon_Ride.gpx")
    list_of_data = decode.get_all_track_point_data_from_gpx()
    # print(list_of_data[1].trkpt.popitem())
    time = list_of_data[1].time
    t1 = time.split("T")
    date_time = t1[0] + " " + t1[1][:-1]

    data = [
        1,
        "point",
        list_of_data[1].ele,
        list_of_data[1].atemp,
        list_of_data[1].hr,
        list_of_data[1].cad,
        date_time
    ]

    print(type(data))

    c = Connection()
    c.query_insert_file_row_into_db(data)


if __name__ == "__main__":
    # exit(main())
    main()
