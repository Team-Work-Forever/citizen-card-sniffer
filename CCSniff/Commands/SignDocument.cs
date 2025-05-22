
using System.CommandLine;
using pt.portugal.eid;

namespace CCSniff.Commands;

public static class SignDocument
{
    private readonly static string _location = "Lisboa, Portugal";
    private readonly static string _reason = "Assinar documento";

    public static Command Create()
    {
        var card = Card.GetCard();
        var command = new Command("sign", "Sign documents with the card");

        var code = new Option<string>("--code", description: "Code for activating request");
        command.AddOption(code);

        var path = new Option<string>("--path", description: "File path");
        command.AddOption(path);

        var destPath = new Option<string>("--out", description: "destination path");
        command.AddOption(destPath);

        command.SetHandler((code, path, destPath) =>
        {
            if (card.SetPin(code, PTEID_Pin.SIGN_PIN, 3))
            {
                PTEID_PDFSignature signature = new();
                signature.setCustomSealSize(200, 200);
                signature.setSignatureLevel(PTEID_SignatureLevel.PTEID_LEVEL_BASIC);

                signature.addToBatchSigning(path);
                card.Instance.SignPDF(signature, 1, 200, 200, _location, _reason, destPath);
            }
        }, code, path, destPath);

        return command;
    }
}