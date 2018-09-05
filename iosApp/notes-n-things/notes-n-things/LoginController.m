//
//  LoginController.m
//  notes-n-things
//
//  Created by Kyle Derrett on 2014-03-22.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "LoginController.h"

@interface LoginController ()



@end

@implementation LoginController

UITextField *emailField;
UITextField *passField;
UILabel *noticeLabel;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    
    if (self)
    {
    // Custom initialization
    }

    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    
    UIButton *submitBtn = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    [submitBtn setTitle:@"Submit" forState:UIControlStateNormal];
    submitBtn.frame = CGRectMake(193, 493, 366, 45);
    [submitBtn addTarget:self action:@selector(submitBtnPressed:)forControlEvents:UIControlEventTouchUpInside];
    
    [self.view addSubview:submitBtn];
    
    emailField = [[UITextField alloc] initWithFrame:CGRectMake(292, 393, 267, 30)];
    emailField.accessibilityLabel = @"Email Field";
    emailField.borderStyle = UITextBorderStyleRoundedRect;
    emailField.font = [UIFont systemFontOfSize:15];
    emailField.placeholder = @"Please enter your Email";
    emailField.autocorrectionType = UITextAutocorrectionTypeNo;
    emailField.keyboardType = UIKeyboardTypeDefault;
    emailField.returnKeyType = UIReturnKeyDone;
    emailField.clearButtonMode = UITextFieldViewModeWhileEditing;
    emailField.contentVerticalAlignment = UIControlContentVerticalAlignmentCenter;
    
    emailField.text = [[NSUserDefaults standardUserDefaults] stringForKey:@"email"];
    
    [self.view addSubview:emailField];
    
    passField = [[UITextField alloc] initWithFrame:CGRectMake(292, 443, 267, 30)];
    passField.accessibilityLabel = @"Password Field";
    passField.borderStyle = UITextBorderStyleRoundedRect;
    passField.font = [UIFont systemFontOfSize:15];
    passField.placeholder = @"Please enter your Password";
    passField.autocorrectionType = UITextAutocorrectionTypeNo;
    passField.keyboardType = UIKeyboardTypeDefault;
    passField.returnKeyType = UIReturnKeyDone;
    passField.clearButtonMode = UITextFieldViewModeWhileEditing;
    passField.contentVerticalAlignment = UIControlContentVerticalAlignmentCenter;
    [passField setSecureTextEntry:YES];
    
    passField.text = [[NSUserDefaults standardUserDefaults] stringForKey:@"password"];
    
    [self.view addSubview:passField];
    
    UIButton *logoutBtn = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    [logoutBtn setTitle:@"Forget Me" forState:UIControlStateNormal];
    logoutBtn.frame = CGRectMake(193, 545, 366, 45);
    [logoutBtn addTarget:self action:@selector(logoutBtnPressed:)forControlEvents:UIControlEventTouchUpInside];
    
    [self.view addSubview:logoutBtn];
    
    noticeLabel = [[UILabel alloc] initWithFrame:CGRectMake(193, 343, 366, 45)];
    noticeLabel.textAlignment = NSTextAlignmentCenter;
    noticeLabel.textColor = [UIColor redColor];
    noticeLabel.text = @"";
    noticeLabel.enabled = NO;
    
    [self.view addSubview:noticeLabel];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)submitBtnPressed:(id)sender
{
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setURL:[NSURL URLWithString:@"http://notes-n-things.tk/api/users"]];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json;charset=UTF-8" forHTTPHeaderField:@"Content-Type"];
    
    NSURLResponse *response;
    NSData *allUsersData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
    
    NSError *error;
    NSMutableDictionary *allUsers = [NSJSONSerialization JSONObjectWithData:allUsersData options:NSJSONReadingMutableContainers error:&error];
    
    if (error) {
        UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Unable to access data" message:@"Currently unable to access the data stored on the server" delegate:self cancelButtonTitle:@"Cancel" otherButtonTitles:nil];
        [alert show];
    }
    
    else {
        NSArray *usersArray = allUsers[@"users"];
        BOOL inpass = NO;

        for (NSDictionary *user in usersArray){
            if ([emailField.text isEqualToString:user[@"email"]]){
                if ([[passField.text stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceCharacterSet]] isEqualToString:[user[@"password"] stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceCharacterSet]]]){
                    [[NSUserDefaults standardUserDefaults] setObject:emailField.text forKey:@"email"];
                    [[NSUserDefaults standardUserDefaults] setObject:passField.text forKey:@"password"];
                    [[NSUserDefaults standardUserDefaults] setObject:user[@"uid"] forKey:@"uid"];
                    [self.navigationController popToRootViewControllerAnimated:TRUE];
                } else {
                    noticeLabel.text = @"Incorrect Password";
                    inpass = YES;
                }
            }
        }
        if (!inpass){
            noticeLabel.text = @"Incorrect Email";
        }
    }
}

- (IBAction)logoutBtnPressed:(id)sender
{
    noticeLabel.text = @"Who are you again?";
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"email"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"password"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"uid"];
    emailField.text = @"";
    passField.text = @"";
}

@end
