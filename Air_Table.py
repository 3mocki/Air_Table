import csv

# Refer to Calibration Data sheet for 26-000160
# NO2 ppb has range from 0 to 2049
# n is selected between 20 degree celcius and 30 degree celcius

# CSV file Column
column = []
row = []
sens = [.228, .399, .267, .318] # mV
weoff = 295 # mV
aeoff = 282 # mV
we = 0
ppb = 0
delta = 4.8 * 10
n = 1.18

def column_Build():
    for i in range(0, 2050):
        column.append(i)
        
def row_Build():
    for i in range(0, 1025):
        row.append(i)

def no2_Table():
    with open("no2_Table.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(column)
        f.close()
        # writer.writerows(row)


    # we = sens * ppb + n(ae - aeoff) + weoff
    #
    # for i in range(0,2050):
    #     ae =


if __name__ == '__main__':
    print("Build NO2 Table")
    column_Build()
    row_Build()
    no2_Table()
