//
//  noteController.m
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-05.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "noteController.h"

extern NSString *noteTitle;
extern NSString *noteId;

@implementation noteController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    NSMutableString *url = [NSMutableString stringWithString:@"http://notes-n-things.tk/api/notes/"];
    [url appendString:noteId];
    [request setURL:[NSURL URLWithString:[NSString stringWithString:url]]];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json;charset=UTF-8" forHTTPHeaderField:@"Content-Type"];
    
    NSURLResponse *response;
    NSData *allNotesData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
    
    NSError *error;
    NSMutableDictionary *note = [NSJSONSerialization JSONObjectWithData:allNotesData options:NSJSONReadingMutableContainers error:&error];
    
    if (error) {
        
        NSLog(@"%@", [error localizedDescription]);
        
        CGRect labelFrame = CGRectMake(75, 125, 618, 20);
        UILabel *noteLabel = [[UILabel alloc] initWithFrame:labelFrame];
        
        [noteLabel setText:@"error loading note; please try again"];
        [noteLabel setNumberOfLines:0];
        [noteLabel setTextAlignment:NSTextAlignmentCenter];
        [noteLabel setTextColor:[UIColor redColor]];
        [self.view addSubview:noteLabel];
        
    }
    
    else {
        CGRect labelFrame = CGRectMake(75, 125, 618, 825);
        UILabel *noteLabel = [[UILabel alloc] initWithFrame:labelFrame];
        
        self.navigationItem.title = noteTitle;
        NSString *text = [NSString stringWithString:note[@"contents"]];
        [noteLabel setText:text];
        [noteLabel setNumberOfLines:0];
        [noteLabel setTextAlignment:NSTextAlignmentLeft];
        [noteLabel sizeToFit];
        [self.view addSubview:noteLabel];
    }
}
@end
