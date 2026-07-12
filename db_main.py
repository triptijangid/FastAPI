from db_tables import create_all_tables
from db_crud_op import insert_user, insert_post, get_user_by_id, get_all_users, get_post_by_user_id, update_user_name, delete_user_by_id

create_all_tables()

insert_user('Tripti', 'tripti@gmail.com', 'kota')
insert_user('yash', 'yash@gmail.com', 'banglore')
insert_user('ronak', 'ronak@gmail.com', 'jaipur')

insert_post(1, "Agentic AI")
insert_post(2, 'Data Science')
insert_post(3, 'Machine Learning')
insert_post(1, 'Java')
insert_post(2, 'JavaScript')

print(get_user_by_id(1))

print(get_all_users())

print(get_post_by_user_id(2))

print(get_user_by_id(2))
update_user_name(2, 'Parmesh Kumar')

delete_user_by_id(1)