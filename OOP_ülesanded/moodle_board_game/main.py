from statistics import Statistics

if __name__ == "__main__":
    stats = Statistics("test_file.csv")

    print("Players:", stats.get("/players"))
    print("Games:", stats.get("/games"))
    print("Total games:", stats.get("/total"))

    print("Joosep played:", stats.get("/player/joosep/amount"))
    print("Joosep favourite:", stats.get("/player/joosep/favourite"))
    print("Joosep wins:", stats.get("/player/joosep/won"))
