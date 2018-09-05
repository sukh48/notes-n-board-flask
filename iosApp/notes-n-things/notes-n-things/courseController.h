//
//  courseController.h
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-05.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "noteController.h"

@interface courseController : UIViewController
{
    IBOutlet NSString *courseTitle;
    
}
@property (nonatomic, strong) IBOutlet UILabel *courseLabel;

@end
