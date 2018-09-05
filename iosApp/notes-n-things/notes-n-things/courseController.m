//
//  courseController.m
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-05.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "courseController.h"

extern NSString *courseName;
extern NSString *courseId;
extern NSString *noteTitle;
extern NSString *noteId;


@implementation courseController

@synthesize courseLabel;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    self.navigationItem.title = courseName;
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    NSMutableString *url = [NSMutableString stringWithString:@"http://notes-n-things.tk/api/notes?q={\"filters\":[{\"name\":\"courseid\",\"op\":\"eq\",\"val\":\""];
    [url appendString:courseId];
    [url appendString:@"\"}]}"];
    NSURL *theurl = [NSURL URLWithString: [url stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding]];
    [request setURL:theurl];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json;charset=UTF-8" forHTTPHeaderField:@"Content-Type"];
    
    NSURLResponse *response;
    NSData *allNotesData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
    
    NSError *error;
    NSMutableDictionary *allNotes = [NSJSONSerialization JSONObjectWithData:allNotesData options:NSJSONReadingMutableContainers error:&error];
    
    if (error) {
        
        NSLog(@"%@", [error localizedDescription]);
        
        CGRect labelFrame = CGRectMake(75, 125, 618, 20);
        UILabel *noteLabel = [[UILabel alloc] initWithFrame:labelFrame];
        
        [noteLabel setText:@"error loading notes; please try again"];
        [noteLabel setNumberOfLines:0];
        [noteLabel setTextAlignment:NSTextAlignmentCenter];
        [noteLabel setTextColor:[UIColor redColor]];
        [self.view addSubview:noteLabel];
    }
    
    else {
        NSArray *notesArray = allNotes[@"notes"];
        
        float _height = 25;
        float _y = 110;
        for (NSDictionary *note in notesArray){
            
            UIButton *noteBtn = [UIButton buttonWithType:UIButtonTypeRoundedRect];
            [noteBtn setTitle:[NSString stringWithFormat:@" %@\n", note[@"file_name"]]forState:UIControlStateNormal];
            [noteBtn setContentHorizontalAlignment:UIControlContentHorizontalAlignmentLeft];
            [noteBtn setFrame:CGRectMake(75, _y, 300, _height)];
            [noteBtn setTag:(NSInteger)[note[@"id"] intValue]];
            [noteBtn addTarget:self action:@selector(noteDetail:) forControlEvents:UIControlEventTouchUpInside];
            
            [self.view addSubview:noteBtn];
            _y = _y + _height;
            
            NSLog(@"---");
            NSLog(@"name %@", note[@"file_name"]);
            NSLog(@"alt Name %@", note[@"contents"]);
            NSLog(@"uid %@", note[@"uid"]);
            NSLog(@"---");
            
        }
    }

}

- (IBAction)noteDetail:(id)sender
{
    noteTitle = [(UIButton *)sender currentTitle];
    noteId = [NSString stringWithFormat:@"%i",((UIButton *)sender).tag ];
    noteController *noteControllerView = [self.storyboard instantiateViewControllerWithIdentifier:@"noteControllerView"];
    [self.navigationController pushViewController:noteControllerView animated:YES];
}
@end
