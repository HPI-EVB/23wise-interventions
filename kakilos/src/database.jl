using LibPQ
using Tables

conn = LibPQ.Connection(
    "host=$(ENV["DB_HOST"]) port=$(ENV["DB_PORT"]) dbname=$(ENV["DB_NAME_SEMINAR2"]) user=$(ENV["DB_USER"]) password=$(ENV["DB_PW"])"
)

function read_sql(statement::String)::Vector{NamedTuple}
    result = LibPQ.execute(conn, statement)
    return rowtable(result)
end
