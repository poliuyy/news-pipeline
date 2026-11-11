create table if not exists news (
    id serial primary key, 
    title text not null, 
    url text not null unique, 
    published timestamptz, 
    source text, 
    loaded_at timestamptz);