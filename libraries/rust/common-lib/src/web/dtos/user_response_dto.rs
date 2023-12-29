pub struct UserResponseDto {
    user_id: Option<Uuid>,
    user_name: Option<String>,
    email: Option<String>,
    date_time_created: Option<DateTime<Utc>>,
    date_time_updated: Option<DateTime<Utc>>,
}
