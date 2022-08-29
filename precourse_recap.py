name = "Steve"
fav_thing = "mining"

dirt = 64
cobble = 128
deepslate = 64
granite = 0
clay = 333
terracotta = 16

total_blocks = dirt + cobble + deepslate + granite + clay + terracotta

print("My name is " + name + ".")
print("My favourite thing is " + fav_thing + ".")
print("I have mined " + str(dirt) + " blocks of dirt!")
print("In total, I have mined " + str(total_blocks) + " blocks!")