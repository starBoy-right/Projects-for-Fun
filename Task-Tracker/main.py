import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Kelola Tugas dari Terminal")

    subparsers = parser.add_subparsers(dest="command", help="Daftar Perintah")
    
    # Route add
    add_parser = subparsers.add_parser("add", help="tambah tugas baru")
    add_parser.add_argument("description", type=str, help="Deskripsi task yang ingin ditambahkan")

    # set up route update
    update_parser = subparsers.add_parser("update", help="Update deskripsi task yang ada")
    update_parser.add_argument("id", type=int, help="ID dari task")
    update_parser.add_argument("description", type=str, help="deskripsi baru")

    # set up route delete
    delete_parser = subparsers.add_parser("delete", help="Hapus task berdasarkan Id")
    delete_parser.add_argument("id", type=int, help="Id dari task yang akan dihapus")

    # Set up route List task
    list_task = subparsers.add_parser("list", help="Daftar Tugas")
    list_task.add_argument("status", type=str, nargs="?", choices=['done', 'todo', 'in-progress'], help="Filter task berdasarkan status")

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Tanda task sedang dikerjakan")
    mark_in_progress_parser.add_argument("id", type=int, help="ID dari task")

    # route mark-done
    mark_in_done_progress = subparsers.add_parser("mark-in-done", help="Tandai task sudah selesai")
    mark_in_done_progress.add_argument("id", type=int, help="ID dari task")

    args = parser.parse_args()

    if args.command == "add":
        print(f"[Aksi] Menambahkan task dengan deskripsi: '{args.description}'")

    elif args.command == "update":
        print(f"[Aksi] Menghapus task ID {args.id}")

    elif args.command == "list":
        if args.status:
            print(f"[Aksi] Menampilkan task dengan status: {args.status}")
        else:
            print(f"[Aksi] Menampilkan semua task")

    elif args.command == "mark-in-progress":
        print(f"[Aksi] Mengubah status task ID {args.id} menjadi in-progress")

    elif args.command == "mark-done":
        print(f"[Aksi] Mengubah status task ID {args.id} menjadi done")

    else:
        parser.print_help()
    


if __name__ == "__main__":
    main()