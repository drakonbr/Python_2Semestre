while True:
    print(f"\033[34m{separador}\033[m\n")
    inicar = input("{:^34}".format("ENTER PARA INICIAR"))
    if inicar != "9999":
        main()
    else:
        print("\033[31mOpção inválida.\033[m")
