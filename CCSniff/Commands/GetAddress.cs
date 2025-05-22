using System.CommandLine;
using pt.portugal.eid;

namespace CCSniff.Commands;

public static class GetAddress
{
    public static Command Create()
    {
        var card = Card.GetCard();
        var command = new Command("address", "Fetch the address from the card");

        var option = new Option<string>("--code", description: "Code for activating request");
        command.AddOption(option);

        command.SetHandler(code =>
        {
            if (card.SetPin(code, PTEID_Pin.ADDR_PIN, 3))
            {
                var address = card.Instance.getAddr();

                Console.WriteLine($"DISTRICT: {address.getDistrict()}");
                Console.WriteLine($"MUNICIPALITY: {address.getMunicipality()}");
                Console.WriteLine($"STREET_NAME: {address.getStreetName()}");
                Console.WriteLine($"CIVIL_PARISH: {address.getCivilParish()}");
                Console.WriteLine($"FLOOR: {address.getFloor()}");
                Console.WriteLine($"DOOR_N: {address.getDoorNo()}");
                Console.WriteLine($"SIDE: {address.getSide()}");
                Console.WriteLine($"PLACE: {address.getPlace()}");
                Console.WriteLine($"LOCALITY: {address.getLocality()}");
                Console.WriteLine($"ZIP: {address.getZip3()}-{address.getZip4()}");
                Console.WriteLine($"POSTAL_LOCALITY: {address.getPostalLocality()}");
            }
        }, option);

        return command;
    }
}