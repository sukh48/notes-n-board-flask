//
//  coursesController.m
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-03.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "coursesController.h"

@implementation coursesController

NSString *courseName = @"";
NSString *courseId = @"";


- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    
    coursesList.text = @"Courses:";
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setURL:[NSURL URLWithString:@"http://notes-n-things.tk/api/courses"]];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json;charset=UTF-8" forHTTPHeaderField:@"Content-Type"];
    
    NSURLResponse *response;
    NSData *allCoursesData= [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
    
    NSError *error;
    NSMutableDictionary *allCourses = [NSJSONSerialization JSONObjectWithData:allCoursesData options:NSJSONReadingMutableContainers error:&error];
    
    if (error) {
        
        NSLog(@"%@", [error localizedDescription]);
        
        CGRect labelFrame = CGRectMake(75, 125, 618, 20);
        UILabel *noteLabel = [[UILabel alloc] initWithFrame:labelFrame];
        
        [noteLabel setText:@"error loading courses; please try again"];
        [noteLabel setNumberOfLines:0];
        [noteLabel setTextAlignment:NSTextAlignmentCenter];
        [noteLabel setTextColor:[UIColor redColor]];
        [self.view addSubview:noteLabel];
    }
    
    else {
        
        NSArray *coursesArray = allCourses[@"courses"];
        
        float _height = 25;
        float _y = 110;
        for (NSDictionary *course in coursesArray){
            
            UIButton *courseBtn = [UIButton buttonWithType:UIButtonTypeRoundedRect];
            [courseBtn setTitle:[NSString stringWithFormat:@" %@\n", course[@"name"]]forState:UIControlStateNormal];
            [courseBtn setFrame:CGRectMake(10, _y, 200, _height)];
            [courseBtn setTag:(NSInteger)[course[@"id"] intValue]];
            [courseBtn addTarget:self action:@selector(courseDetail:)  forControlEvents:UIControlEventTouchUpInside];
  
            [self.view addSubview:courseBtn];
            _y = _y + _height;
            
            NSLog(@"---");
            NSLog(@"name %@", course[@"name"]);
            NSLog(@"alt Name %@", course[@"alt_name"]);
            NSLog(@"courseid %@", course[@"id"]);
            NSLog(@"---");
        }
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)courseDetail:(id)sender
{
    courseName = [(UIButton *)sender currentTitle];
    courseId = [NSString stringWithFormat:@"%i",((UIButton *)sender).tag ];
    courseController *courseControllerView = [self.storyboard instantiateViewControllerWithIdentifier:@"courseControllerView"];
    [self.navigationController pushViewController:courseControllerView animated:YES];
}


@end









