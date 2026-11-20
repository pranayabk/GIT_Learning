# learning various function of python honestly
height ={
    'BOB': 5.67,
    'Jake': 6.00,
    'Mei': 4.11,
}
ave_height = sum(height.values())/len(height)
tallest_person= max(height, keys=height.get)
def feet_in_dec_to_cm (val=float)->float:
    #separting the values feet and inches values:
    feet = int(val)
    inches = ()