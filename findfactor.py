def factor_monic_quadratic_trinomial( b, c):
    a = 1
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if discriminant is non-negative
    if discriminant >= 0:
        # Calculate solutions
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        
        print (b)
        print (c)
        # Return the factorized form
        if x1>=0 and x2>=0:
             return f"(x - {x1:.2f})(x - {x2:.2f})"
        else :
            if x1>=0 and x2<0:
                x2 = -1 * x2
                return f"(x - {x1:.2f})(x + {x2:.2f})"
            else:
                if x1<0 and x2>=0:
                    x1 = -1 * x1
                    return f"(x + {x1:.2f})(x - {x2:.2f})"
                else:
                    x1 = -1 * x1
                    x2 = -1 * x2
                    return f"(x + {x1:.2f})(x + {x2:.2f})"
                        
                
    else:
        return "Cannot factorize (complex roots)"


 

b = -5
c = -24
result = factor_monic_quadratic_trinomial( b, c)
print(result)  # Output: 2(x + 2.00)(x + 1.00)