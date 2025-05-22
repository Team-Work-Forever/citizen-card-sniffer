
using System.CommandLine;

namespace CCSniff.Commands;

public static class GetUser
{
    public static Command Create()
    {
        var card = Card.GetCard();
        var command = new Command("info", "Fetch user details");

        command.SetHandler(() =>
        {
            var info = card.Instance.getID();

            Console.WriteLine($"SURNAME: {info.getSurname()}");
            Console.WriteLine($"GIVEN_NAME: {info.getGivenName()}");
            Console.WriteLine($"SEX: {info.getGender()}");
            Console.WriteLine($"HEIGHT: {info.getHeight()}");
            Console.WriteLine($"NATIONALITY: {info.getNationality()}");
            Console.WriteLine($"BIRTHDATE: {info.getDateOfBirth()}");
            Console.WriteLine($"N_DOCUMENT: {info.getDocumentNumber()}");
            Console.WriteLine($"VALID_DATE: {info.getValidityBeginDate()} {info.getValidityEndDate()}");
            Console.WriteLine($"MOTHER_SURNAME: {info.getSurnameMother()}");
            Console.WriteLine($"MOTHER_GIVEN_NAME: {info.getGivenNameMother()}");
            Console.WriteLine($"FATHER_SURNAME: {info.getSurnameFather()}");
            Console.WriteLine($"FATHER_GIVEN_NAME: {info.getGivenNameFather()}");
            Console.WriteLine($"NIF: {info.getCivilianIdNumber()}");
            Console.WriteLine($"SOCIAL_SECURITY: {info.getSocialSecurityNumber()}");
            Console.WriteLine($"HEALTH: {info.getHealthNumber()}");
        });

        return command;
    }
}