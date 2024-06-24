from models.PrimateDAO import PrimateDAO

def main():
    primate: PrimateDAO = PrimateDAO("storage/data/primates_dataset.csv")
    print(primate.data)

if __name__ == "__main__":
    main()