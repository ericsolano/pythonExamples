def http_error(status):

    print("http status: ", status)

    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

def logic_match(some_logic):


    match some_logic:
         case True:
              return "Statement is TRUE"
         case False:
              return "Statement is FALSE"      



def where_is_point01(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")



print( http_error(400) )
print( http_error(404) )
print( http_error(401) )
print( http_error(418) )

print( logic_match(3**2==9))
print( logic_match(1==2))

where_is_point01((0,0))
where_is_point01((1,1))

