using System;
using CommonLib.Domain.Models;


// To leverage the functionalities offered by the CommonLib nuget package, access the 'Setup' view within the NuGet package and perform the following steps:
// 0. dotnet nuget add source --name <> --username <> --password <> --store-password-in-clear-text <> 
// 1. dotnet add package CommonLib -v <package version, e.g. 0.1.0-dev12> -s <>
class Program
{
    static void Main()
    {
        var user = new User
        {
            userName = "ValidUserName",
            userPassword = "StrongPassword123!",
            email = "test@example.com",
            userId = Guid.NewGuid(),
            dateTimeCreated = DateTime.Now,
            dateTimeUpdated = DateTime.Now
        };

        PrintUserAttributes(user);
    }

    static void PrintUserAttributes(User user)
    {
        Console.WriteLine("User Attributes:");
        Console.WriteLine($"User Name: {user.userName}");
        Console.WriteLine($"User Password: {user.userPassword}");
        Console.WriteLine($"Email: {user.email}");
        Console.WriteLine($"User ID: {user.userId}");
        Console.WriteLine($"Date Time Created: {user.dateTimeCreated}");
        Console.WriteLine($"Date Time Updated: {user.dateTimeUpdated}");
    }
}
