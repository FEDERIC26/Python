# Calculatrice de moyenne générale du BAC avec mentions

# mention très bien (TB) : pour une moyenne entre 16 et 18.
# mention bien (B) : pour une moyenne entre 14 et 16 ;
# mention assez bien (AB) : pour une moyenne entre 12 et 14 ;

moyenne =  float(input("Entrer votre moyenne générale:"))

if 18<= moyenne < 20:
    print("Les félicitations du Jury")
elif 16<= moyenne < 18   :
    print("Vous avez obtenu mention Très bien")
elif 14 <= moyenne < 16  :
    print("Vous avez obtenu mention Assez Bien")
elif 12 <= moyenne < 14  :
    print("Vous avez obtenu mention Bien")   
else: 
    print("Vous n'avez pas obtenu de mention")
