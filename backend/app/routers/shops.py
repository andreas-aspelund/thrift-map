from fastapi import APIRouter, HTTPException
from ..database import get_connection

router = APIRouter(prefix="/shops", tags=["shops"])


@router.get("")
def list_shops():
    """Return all shops ordered by name."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, name, address, lat, lng, neighborhood, notes, created_at
                FROM shops
                ORDER BY name
                """
            )
            rows = cur.fetchall()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


@router.get("/{shop_id}")
def get_shop(shop_id: int):
    """Return a single shop by id."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, name, address, lat, lng, neighborhood, notes, created_at
                FROM shops
                WHERE id = %s
                """,
                (shop_id,),
            )
            row = cur.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Shop not found")
        return dict(row)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
