using pt.portugal.eid;

public class Card
{
    private readonly PTEID_EIDCard _card;

    public PTEID_EIDCard Instance => _card;

    public Card(PTEID_EIDCard card)
    {
        _card = card;
    }

    public bool SetPin(string input, uint type, uint tries)
    {
        PTEID_Pins pins = _card.getPins();
        var pin = pins.getPinByPinRef(type);

        return pin.verifyPin(input, ref tries, true);
    }

    public static Card GetCard()
    {
        PTEID_ReaderSet readerSet = PTEID_ReaderSet.instance();

        var context = readerSet.getReader();

        if (context.isCardPresent())
        {
            return new Card(context.getEIDCard());
        }

        throw new Exception("Card is not inserted");
    }

}