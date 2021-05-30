# %%
import sqlite3

    # questions
    # add
    # change
    # delete
    # search

def UI(cur):
    print("---------------")
    print("1.Add")
    print("---------------")
    print("2.Display Table")
    print("---------------")
    print("3.Delete")
    print("---------------")
    print("4.Change")
    print("---------------")

    val_list = []
    col_list = []
    table = ""
    good_select = True
    while good_select:
        choice = input().upper()
        good_select = False
        if (choice == "ADD" or choice == "1"):
            display_val("table".upper(),cur)
            table = input("Which table do you want to add to?").lower()
            more = True
            col_list =  []
            while more:
                display_val('column'.lower(),cur,table)
                col_list.append(input("Which column do you want to add to?").lower())
                more = input("Any More?(y/n)")
                if more.lower() == 'n':
                    more = False
                else:
                    more = True
            more = True
            list_list = []
            while more:
                val_list =  []
                for col in col_list:
                    val_list.append(input("What values do you want in {}:".format(col)))
                list_list.append(val_list)
                more = input("Any More?(y/n)")
                if more.lower() == 'n':
                    more = False
                else:
                    more = True
            add_s = add(table,col_list,list_list)
            cur.execute(add_s)
            display_val('whole'.lower(),cur,table)
        elif(choice == "DISPLAY_TABLE" or choice == "2"):
            display(cur,choice)
        elif (choice == "DELETE" or choice == "3"): 
            table = display(cur,choice)
            deleting =  True
            condition = []
            while deleting:
                condition.append(input("Which row?"))
                statement = delete(table,condition)
                cur.execute(statement)
                display_val("whole".lower(),cur,table)
                more = input("Any More?(y/n)")
                if more.lower() == 'n':
                    deleting = False
                else:
                    deleting = True

        elif(choice == "CHANGE" or choice == "4"):
            table, col = display(cur,choice)
            changing = True

            while changing:
                row = input("Which value? ")
                new_val = input("To what value?")
                change_s = change(table,col,row,new_val)
                cur.execute(change_s)
                
                
                display_val("whole".lower(),cur,table)
                more = input("Any More?(y/n)")
                if more.lower() == 'n':
                    changing = False
                else:
                    changing = True
        else:
            print("Please select from the objects listed.")
            good_select = True
        



    # get table list
    # display table
    # get col list
    # get val list

    # Get Connection

def display(cur,choice):
    display_val("table".upper(),cur)
    table = input("which table?")
    display_val("column".lower(),cur,table)
    if (choice == "CHANGE" or choice == "4"):
        col = input("which column?")
        display_val("whole".lower(),cur,table)
        return table, col
    else:
        display_val("whole".lower(),cur,table)
    return table

def display_val(val,cur,table = 'product',column = 'name'):
    if val.lower() == 'table':
        cur.execute('''SELECT name FROM sqlite_master WHERE type='{}';'''.format(val.lower()))
        results = cur.fetchall()
    elif val.lower() == 'column':
        cur.execute("""SELECT * FROM {}""".format(table.lower()))
        results = cur.description
        print("---------------")
        print(results[0][0]+ ' | ' +results[1][0])
        return -144
    elif val.lower() == 'whole':
        cur.execute("""SELECT * FROM {}""".format(table.lower()))
        results = cur.fetchall()
        for row in results:
            print("---------------")
            print(row[0], ' | ' + row[1])
        return -144
    for value in results:
        print("---------------")
        print(value[0])
    return -144



def delete(table,condition):
    a = """DELETE FROM {} WHERE {}_id """.format(table,table)
    if len(condition) > 1:
        a += """IN ("""
        for iterate,val in enumerate(condition):
            if iterate == 0:
                a += """ {} """.format(val) 
            else:
                a += """, {} """.format(val) 
        a += """ ) """
    else:
        a += """ = {}""".format(condition[0])
    return a

def change(table,col,row,new_val):
    if isinstance(new_val, str):
        new_val = "\'{}\'".format(new_val)
    a = """ UPDATE {}
            SET {} = {}
            WHERE {}_id = {}""".format(table,col,new_val,table,row)
    return a


def add(table,list_col,list_val):
    #list of col
    a = """INSERT INTO {}('{}')VALUES""".format(table,'\',\''.join(list_col))
    for iterate, lists in enumerate(list_val):
        for values in lists:
            if len(lists) > 1:
                a += "('{}')".format('\',\''.join(values))
            else:
                a += "('{}')".format(values)
        if iterate == len(list_val)-1:
            pass
        elif len(list_val) > 1:
            a += ","
    return a

def main():
    con = sqlite3.connect("test.db", timeout=30)
    cur = con.cursor()
    UI(cur)
    con.commit()
    con.close()

if __name__ == "__main__" :
    main()
# %%
