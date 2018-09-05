//
//  notes_n_thingsTests.m
//  notes-n-thingsTests
//
//  Created by Kyle Derrett on 2/26/2014.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "notes_n_thingsTests.h"

@implementation notes_n_thingsTests

- (void)setUp
{
    [super setUp];
    
    // Set-up code here.
}

- (void)tearDown
{
    // Tear-down code here.
    
    [super tearDown];
}

//login relies on NSUserDefaults test them to make sure it works
- (void)testUsingNSUserDefaults
{
    //they can be set to empty strings and not remain nil
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"email"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"password"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"uid"];
    STAssertNotNil([[NSUserDefaults standardUserDefaults] stringForKey:@"email"], @"Can't set user default email with empty string");
    STAssertNotNil([[NSUserDefaults standardUserDefaults] stringForKey:@"password"], @"Can't set user default password with empty string");
    STAssertNotNil([[NSUserDefaults standardUserDefaults] stringForKey:@"uid"], @"Can't set user default uid with empty string");
    
    //they can be set to specific values
    [[NSUserDefaults standardUserDefaults] setObject:@"someEmail" forKey:@"email"];
    [[NSUserDefaults standardUserDefaults] setObject:@"somePass" forKey:@"password"];
    [[NSUserDefaults standardUserDefaults] setObject:@"1" forKey:@"uid"];
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"email"], @"someEmail", @"Can't set user default email with string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"password"], @"somePass", @"Can't set user default password with empty string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"uid"], @"1", @"Can't set user default uid with empty string");
    
    //can be set to empty strings after being set to a string
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"email"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"password"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"uid"];
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"email"], @"", @"Can't set user default email with string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"password"], @"", @"Can't set user default password with empty string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"uid"], @"", @"Can't set user default uid with empty string");
}

//make sure we get the course we know is in the database
- (void)testGettingCourses
{
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    //using dev3 the test server
    [request setURL:[NSURL URLWithString:@"http://dev3.notes-n-things.tk/api/courses"]];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json;charset=UTF-8" forHTTPHeaderField:@"Content-Type"];
    
    NSURLResponse *response;
    NSData *allCoursesData= [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
    
    NSError *error;
    NSMutableDictionary *allCourses = [NSJSONSerialization JSONObjectWithData:allCoursesData options:NSJSONReadingMutableContainers error:&error];
    
    if (error) {
        
        NSLog(@"%@", [error localizedDescription]);
        
    }
    
    else {
        
        NSArray *coursesArray = allCourses[@"courses"];
        NSString *firstCourse = coursesArray[0][@"name"];
        STAssertTrue([firstCourse isEqualToString:@"COMP 1010"], @"Make sure we get the course used as a test");
    }
}

// test getting the notes once it is up and running
- (void)testGettingNotes
{
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    //using dev3 as a test server
    [request setURL:[NSURL URLWithString:@"http://dev3.notes-n-things.tk/api/notes"]];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json;charset=UTF-8" forHTTPHeaderField:@"Content-Type"];
    
    NSURLResponse *response;
    NSData *allNotesData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
    
    NSError *error;
    NSMutableDictionary *allNotes = [NSJSONSerialization JSONObjectWithData:allNotesData options:NSJSONReadingMutableContainers error:&error];
    
    if (error) {
        
        NSLog(@"%@", [error localizedDescription]);

    }
    
    else {
        NSArray *notesArray = allNotes[@"notes"];
        NSString *firstNote = notesArray[0][@"file_name"];
        STAssertTrue([firstNote isEqualToString:@"Lecture 1"], @"Make sure we get the note used as a test");
    }
}


@end
