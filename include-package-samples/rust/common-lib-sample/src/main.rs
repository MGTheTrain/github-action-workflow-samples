use chrono::{DateTime, Utc};
use uuid::Uuid;
use common_lib::domain::models::user::User;

fn main() {
    let user_id = Some(Uuid::new_v4());
    let user = User {
        user_id,
        user_name: Some("JohnDoe".to_string()),
        user_password: Some("password123".to_string()),
        email: Some("johndoe@example.com".to_string()),
        date_time_created: Some(Utc::now()),
        date_time_updated: Some(Utc::now()),
    };

    // Print User Attributes
    println!("User Attributes:");
    println!("User ID: {:?}", user.user_id);
    println!("User Name: {:?}", user.user_name);
    println!("User Password: {:?}", user.user_password);
    println!("Email: {:?}", user.email);
    println!("Date Time Created: {:?}", user.date_time_created);
    println!("Date Time Updated: {:?}", user.date_time_updated);
}
