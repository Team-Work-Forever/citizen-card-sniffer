using CCSniff.Commands;
using pt.portugal.eid;
using System.CommandLine;

PTEID_ReaderSet.initSDK();

try
{
    var rootCommand = new RootCommand("cc - interacter");

    rootCommand.AddCommand(GetAddress.Create());
    rootCommand.AddCommand(SignDocument.Create());
    rootCommand.AddCommand(GetUser.Create());

    await rootCommand.InvokeAsync(args);
}
catch (Exception e)
{
    Console.WriteLine(e.Message);
}

PTEID_ReaderSet.releaseSDK();