import yaml

class State:

    def __init__(self, json) -> None:
        [self.abbr,self.name,self.region,self.motto,self.pop,self.landlocked] = self.jsonParse(json)

    def __str__(self) -> str:
        if self.landlocked:
            ocean = "Because this state does not border water, you need not worry about the Kraken.\n"
        else:
            ocean = "Because this state does border water, be aware of the Kraken's presence.\n"
        sum =  f"{self.name}, containing {self.pop} people, is in the {self.region} part of the US.\n"
        detail = f"The state motto is \"{self.motto}\".\n"
        return sum + detail + ocean

    def jsonParse(self,fayle):
        abbr = fayle['abbr']
        name = fayle['name']
        region = fayle['region']
        motto = fayle['motto']
        pop = fayle['population']
        landlocked = fayle['landlocked']
        return [abbr,name,region,motto,pop,landlocked]


def main():
    with open("states.yaml") as yam:
        content = yaml.safe_load(yam)
        for state in content:
            st = State(state['state'])
            print(st)
        


if __name__ == "__main__":
    main()