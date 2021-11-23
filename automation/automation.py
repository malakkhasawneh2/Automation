import re

with open('assets/potential-contacts.txt','r')as f:
    file=f.read()

def emails(file):
    
    text_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file)
    match_email=sorted(set(text_email))
    result ='\n'.join(match_email)

    with open('assets/emails.txt','w')as f:
        f.write(result )



def phone_numbers( file ):

    list_of_numbers = []
    match_phone_number = re.findall( r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', file )
    
    for phone in match_phone_number:
        
        if "(" in phone:
            phone = phone.replace( "(", "" )
        if ")" in phone or "." in phone:
            phone = phone.replace( ")", "-" )
            phone = phone.replace( ".", "-" )
        if len( phone ) == 10:
            phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
        if not phone in list_of_numbers:
            list_of_numbers.append( phone )
    list_of_numbers = sorted( list_of_numbers )

    with open( 'assets/phone_numbers.txt', 'w' ) as result:
        for phone in list_of_numbers:
            result.write( f"{phone}\n" )



if __name__ == "__main__":
    email = emails(file)
    list_of_numbers = phone_numbers(file)





