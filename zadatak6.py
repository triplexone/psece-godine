print ("Pseće godine")

ljudske_godine = 4
prve_godine = 10.5
godine = int(input("Koliko pas ima godina? "))

if godine <= 0:
    print("Taj pas se još nije rodio")
elif godine > 2:
    psece_godine = prve_godine * 2 + ((godine - 2) * ljudske_godine)
    print("Pas star " + str(godine) + " ljudske godine ima " + str(psece_godine) + " psećih godina.")
elif godine <= 2:
    psece_godine = prve_godine * godine
    print("Pas star " + str(godine) + " ljudske godine ima " + str(psece_godine) + " psećih godina.")