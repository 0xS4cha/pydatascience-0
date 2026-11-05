ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

def main():
    ft_list.append("world!")
    ft_tuple = ("Hello", "France!")
    ft_set = set(["Paris!", "Hello"])
    ft_dict["Hello"] = "42Paris!"
    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()