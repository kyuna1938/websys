from sqlalchemy.exc import (  # Raised when an error occurs during SQL compilation; Raised when the execution of a database operation fails.; Wraps a DB-API `DataError`.; Wraps a DB-API `DatabaseError`.; Raised by a PoolListener so that the host pool forces a disconnect.; Raised by `ForeignKey` to indicate a reference cannot be resolved.; Raised by `ForeignKey` when the referred Column cannot be located.; Raised by `ForeignKey` when the referred Table cannot be located.; A nonexistent column is requested from a `RowProxy`.; Table does not exist or is not visible to a connection.; Generic error class.
    CompileError, DatabaseError, DataError, DBAPIError, DisconnectionError,
    InvalidRequestError, NoReferencedColumnError, NoReferencedTableError,
    NoReferenceError, NoSuchColumnError, NoSuchTableError, SQLAlchemyError)
from sqlalchemy.orm.exc import (  # A invalid condition was detected during `flush()`.; A refresh() operation failed to re-retrieve an object's row.
    FlushError, ObjectDeletedError)


class APIBaseError(Exception):
    """ BaseError class of following custom errors.
        This might be helpful if we have these custom errors take status code.
    """
    status_code: int


class ResourceNotFoundError(Exception):
    def __str__(self) -> str:
        return f"Resource not found: {super().__str__()}"

    def __repr__(self) -> str:
        return super().__repr__()


class UnauthorizedError(Exception):
    def __str__(self) -> str:
        return f"Unauthorized: {super().__str__()}"

    def __repr__(self) -> str:
        return super().__repr__()


class ConsistencyError(Exception):
    def __str__(self) -> str:
        return f"Consistency error: {super().__str__()}"

    def __repr__(self) -> str:
        return super().__repr__()


# Following custom errors might be unnecessary.
class BadParamterError(Exception):
    def __str__(self) -> str:
        return f"Invalid requested parameters: {super().__str__()}"

    def __repr__(self) -> str:
        return super().__repr__()


class InternalServerError(Exception):
    def __str__(self) -> str:
        return f"Internal server error: {super().__str__()}"

    def __repr__(self) -> str:
        return super().__repr__()


def translate_orm_error(err: SQLAlchemyError) -> Exception:
    """ Return custom error by given SQLAlchemyError

    Args:
        err (SQLAlchemyError) : Error object raised by SQLAlchemy

    Returns:
        Exception : Custom error
    """
    try:
        raise err
    except (
        FlushError,
        NoReferenceError,
        NoReferencedColumnError,
        NoReferencedTableError,
        ObjectDeletedError,
    ) as ref:
        return ConsistencyError(ref)
    except (
        NoSuchColumnError,
        NoSuchTableError
    ) as nf:
        return ResourceNotFoundError(nf)
    except (CompileError, InvalidRequestError) as ir:
        # `InvalidRequestError` may be better
        return InternalServerError(ir)
    except (
            DBAPIError,
            DataError,
            DatabaseError,
            DisconnectionError
    ) as fe:
        # This block is not so important
        return InternalServerError(fe)
    except SQLAlchemyError as e:
        # Other SQLAlchemyError
        return InternalServerError(e)
    except Exception as e:
        # Unknown errors
        return InternalServerError(e)
